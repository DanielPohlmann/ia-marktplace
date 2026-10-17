<!-- Part of the dev-design-patterns-structural skill. Loaded on demand from SKILL.md. -->

# 5. Facade

## Intent
Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

## Structure

```
┌────────────────┐
│     Client      │
└──────┬─────────┘
       │ uses
       ▼
┌─────────────────────────┐
│        Facade            │
├─────────────────────────┤
│ + simpleOperation()      │
└──┬──────┬──────┬────────┘
   │      │      │
   ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐
│Sub-A ││Sub-B ││Sub-C │
│      ││      ││      │
└──────┘└──────┘└──────┘
   Subsystem classes
```

## Participants
- **Facade** — provides simple methods that delegate to subsystem classes; knows which subsystem classes are responsible for a request
- **Subsystem classes** — implement subsystem functionality; handle work assigned by the Facade; have no knowledge of the Facade

## When to Use
- You want to provide a simple interface to a complex subsystem
- There are many dependencies between clients and implementation classes
- You want to layer your subsystems — use a Facade for each level

## TypeScript Example

```typescript
// Subsystem classes
class VideoDecoder {
  decode(file: string): string {
    return `decoded-frames(${file})`;
  }
}

class AudioDecoder {
  decode(file: string): string {
    return `decoded-audio(${file})`;
  }
}

class SubtitleParser {
  parse(file: string): string[] {
    return [`00:01 Hello`, `00:05 World`];
  }
}

class VideoRenderer {
  render(frames: string, audio: string, subs: string[]): string {
    return `Rendering: ${frames} + ${audio} with ${subs.length} subtitles`;
  }
}

// Facade — hides all subsystem complexity
class MediaPlayerFacade {
  private videoDecoder = new VideoDecoder();
  private audioDecoder = new AudioDecoder();
  private subtitleParser = new SubtitleParser();
  private renderer = new VideoRenderer();

  play(videoFile: string, subtitleFile?: string): string {
    const frames = this.videoDecoder.decode(videoFile);
    const audio = this.audioDecoder.decode(videoFile);
    const subs = subtitleFile
      ? this.subtitleParser.parse(subtitleFile)
      : [];
    return this.renderer.render(frames, audio, subs);
  }
}

// Usage — client only knows the Facade
const player = new MediaPlayerFacade();
console.log(player.play("movie.mp4", "movie.srt"));
// Rendering: decoded-frames(movie.mp4) + decoded-audio(movie.mp4) with 2 subtitles
```

---
